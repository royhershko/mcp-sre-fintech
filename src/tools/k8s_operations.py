import logging
from kubernetes import client, config

def get_pod_status(namespace: str = "default"):
    """
    Checks for non-running pods in a specific K8s namespace.
    Helps the agent identify failing components in the trading stack.
    """
    try:
        # Load kubeconfig (works for local and in-cluster)
        try:
            config.load_incluster_config()
        except config.ConfigException:
            config.load_kube_config()

        v1 = client.CoreV1Api()
        pods = v1.list_namespaced_pod(namespace)
        
        unhealthy = [
            f"{p.metadata.name}: {p.status.phase}" 
            for p in pods.items if p.status.phase != "Running"
        ]
        
        if not unhealthy:
            return f"Success: All pods in namespace '{namespace}' are healthy."
        return f"Warning: Unhealthy Pods detected in '{namespace}': " + ", ".join(unhealthy)
    except Exception as e:
        return f"K8s Error: Could not connect to cluster. Details: {str(e)}"
