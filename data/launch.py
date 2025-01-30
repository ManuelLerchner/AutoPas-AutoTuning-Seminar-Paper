import subprocess
import os
from time import sleep
import shutil

SCRIPT_TEMPLATE = """#!/bin/bash

#SBATCH -J EarlyStopping_{{YAML_FILENAME}}_Threads
#SBATCH -o ./%x.%j.%N.out
#SBATCH -D ./AutoPas/build/examples/md-flexible/{{SCENARIO_NAME}}/{{FACTOR}}
#SBATCH --get-user-env
#SBATCH --clusters={{CLUSTER}}
#SBATCH --partition={{PARTITION}}
#SBATCH --mail-type=all
#SBATCH --mem=2000mb
#SBATCH --cpus-per-task=1
#SBATCH --mail-user=manuel.lerchner@tum.de
#SBATCH --export=NONE
#SBATCH --time=06:00:00

sleep $((RANDOM % 120))
../../md-flexible --yaml-filename {{YAML_FILENAME}} --log-level info {{PARAMS}}
"""


def launch_job(scenario, yaml, params, factor, cluster, partition):
    script = SCRIPT_TEMPLATE
    script = script.replace("{{CLUSTER}}", cluster)
    script = script.replace("{{PARTITION}}", partition)
    script = script.replace("{{SCENARIO_NAME}}", scenario)
    script = script.replace("{{YAML_FILENAME}}", yaml)
    script = script.replace("{{FACTOR}}", factor)
    script = script.replace("{{PARAMS}}", params)

    scenario_name = yaml.split(".")[0]
    filename = scenario_name+"_"+params+"_"+str(factor)+".sh"
    with open(filename, "w") as f:
        f.write(script)

    print("Launching job with factor", factor)
    subprocess.call(["sbatch", filename])

    os.remove(filename)
    sleep(10)


def printUsefullCommands():
    expected_compilation_flags = "-DAUTOPAS_LOG_TUNINGDATA=ON -DAUTOPAS_LOG_LIVEINFO=ON -DAUTOPAS_MIN_LOG_LVL=TRACE -DMD_FLEXIBLE_PAUSE_SIMULATION_DURING_TUNING=ON -DAUTOPAS_LOG_TUNINGRESULTS=ON"

    input("Please make sure that the compilation flags are set to: " +
          expected_compilation_flags + "\n\nPress Enter to continue...")

    print("Useful commands:")
    print("squeue --cluster=serial")
    print("scancel --cluster=serial id")
    print("sacct --cluster=serial -X -u ge47wer2")
    print("")


if __name__ == "__main__":
    printUsefullCommands()
    factor = ["1.25", "1.5", "2", "2.5", "3", "5", "7.5", "10",
              "12.5", "15", "20", "25", "250", "100", "500", "1000", "10000"]
    factor = ["2"]
    scenario_name = "explodingLiquid"

    for factor in factor:

        cluster, partition = ("serial", "serial_std")

        # replace factor in new file
        new_scenario_name = scenario_name.split(
            ".")[0] + "-" + factor+".yaml"

        pathname = "md-flexible/"+scenario_name+"/"+factor
        os.makedirs(pathname, exist_ok=True)

        with open("md-flexible/"+scenario_name+".yaml", "r") as f:
            file = f.read()
            file = file.replace("max-allowed-slowdown-factor      :  {}",
                                f"max-allowed-slowdown-factor      :  {factor}")

            with open(pathname+"/"+new_scenario_name, "w") as f2:
                f2.write(file)

        # mkdir

        launch_job(scenario_name, new_scenario_name, "",
                   factor, cluster, partition)
