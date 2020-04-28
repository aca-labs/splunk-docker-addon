[docker_processes://<name>]
docker_api_version = e.g. 1.39. Check with docker version. Leave as 'auto' to automatically detect.
container_ids = Enter list of long container IDs. Obtained from command line 'docker ps -a'. Format as space separated.
module_path = Change only if modules are installed in different location to suggested.

[docker_container_overview://<name>]
docker_api_version = e.g. v1.39

[docker_api_shell_script://<name>]
command = e.g. docker stats --no-stream --format "{\"name\":\"{{ .Name }}\",\"memory\":{\"raw\":\"{{ .MemUsage }}\",\"percent\":\"{{ .MemPerc }}\"},\"cpu\":\"{{ .CPUPerc }}\"}"
override_sourcetype = Recommend overriding sourcetype to something more specific to your call.