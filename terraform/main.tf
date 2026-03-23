terraform {
  required_providers {
    kubernetes = {
      source  = "hashicorp/kubernetes"
      version = ">= 2.0.0"
    }
  }
}

provider "kubernetes" {
  config_path = "~/.kube/config" # Path to your local kubeconfig
}

resource "kubernetes_namespace" "fintech_namespace" {
  metadata {
    name = var.namespace_name
    labels = {
      environment = "production"
      team        = "sre"
    }
  }
}

resource "kubernetes_resource_quota" "fintech_quota" {
  metadata {
    name      = "fintech-quota"
    namespace = kubernetes_namespace.fintech_namespace.metadata[0].name
  }
  spec {
    hard = {
      pods = "10"
      cpu  = "4"
      memory = "8Gi"
    }
  }
}
