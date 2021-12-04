variable "registry_container_name" {
  description = "Value of the name for the Docker Registry"
  type        = string
  default     = "LocalDockerRegistry"
}

variable "local_registry_spawned" {
  description = "Only pull images hosted in local registry if registry is active"
  type        = bool
  default     = false
}

variable "devops_diagram_container_name" {
  description = "Value of the name for the DevOps Diagram"
  type        = string
  default     = "DevopsDiagram"
}