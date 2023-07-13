from kubernetes import client, config

def namespace_exists(namespace_name):
    api_instance = client.CoreV1Api()

    try:
        api_instance.read_namespace(namespace_name)
        return True

    except client.ApiException as e:
        if e.status == 404:
            return False
        else:
            print(f"Error checking namespace: {e}")
            return False

def create_namespace(namespace_name, cpu_limit, memory_limit, cpu_request, memory_request):
    api_instance = client.CoreV1Api()

    if namespace_exists(namespace_name):
        print(f"Namespace '{namespace_name}' already exists.")
        return

    namespace = client.V1Namespace(metadata=client.V1ObjectMeta(name=namespace_name))

    try:
        api_instance.create_namespace(namespace)
        print(f"Namespace '{namespace_name}' created successfully.")

        # Create resource quota
        resource_quota = client.V1ResourceQuota(
            metadata=client.V1ObjectMeta(name=f"quota-{namespace_name}", namespace=namespace_name),
            spec=client.V1ResourceQuotaSpec(
                hard={
                    "limits.cpu": cpu_limit,
                    "limits.memory": memory_limit,
                    "requests.cpu": cpu_request,
                    "requests.memory": memory_request,
                }
            ),
        )
        api_instance.create_namespaced_resource_quota(namespace_name, resource_quota)
        print(f"Resource quota for namespace '{namespace_name}' created successfully.")

    except client.ApiException as e:
        print(f"Error creating namespace: {e}")

# Usage example
if __name__ == "__main__":
    # Load the Kubernetes configuration from the default kubeconfig file
    config.load_kube_config()

    # Set the desired namespace name, CPU limit, memory limit, CPU request, and memory request
    namespace_name = "my-namespace"
    cpu_limit = "2"
    memory_limit = "2Gi"
    cpu_request = "1"
    memory_request = "1Gi"

    # Create the namespace if it doesn't exist and reserve capacity
    create_namespace(namespace_name, cpu_limit, memory_limit, cpu_request, memory_request)
    ==============

import os

def apply_resource_quota(namespace_name, cpu_limit, memory_limit, cpu_request, memory_request):
    command = f"kubectl apply -n {namespace_name} -f - <<EOF\n\
apiVersion: v1\n\
kind: ResourceQuota\n\
metadata:\n\
  name: quota-{namespace_name}\n\
spec:\n\
  hard:\n\
    limits.cpu: {cpu_limit}\n\
    limits.memory: {memory_limit}\n\
    requests.cpu: {cpu_request}\n\
    requests.memory: {memory_request}\n\
EOF"

    try:
        os.system(command)
        print(f"Resource quota applied for namespace '{namespace_name}' successfully.")
    except Exception as e:
        print(f"Error applying resource quota: {e}")

# Usage example
if __name__ == "__main__":
    # Set the desired namespace name, CPU limit, memory limit, CPU request, and memory request
    namespace_name = "my-namespace"
    cpu_limit = "2"
    memory_limit = "2Gi"
    cpu_request = "1"
    memory_request = "1Gi"

    # Apply the resource quota
    apply_resource_quota(namespace_name, cpu_limit, memory_limit, cpu_request, memory_request)

