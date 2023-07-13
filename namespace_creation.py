from kubernetes import client, config

def create_namespace(namespace_name, cpu_limit, memory_limit, cpu_request, memory_request):
    api_instance = client.CoreV1Api()
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

    # Create the namespace and reserve capacity
    create_namespace(namespace_name, cpu_limit, memory_limit, cpu_request, memory_request)
