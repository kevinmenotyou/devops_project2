variable "registry_container_name" {
  description = "Value of the name for the Docker Registry"
  type        = string
  default     = "LocalDockerRegistry"
}

variable "devops_diagram_container_name" {
  description = "Value of the name for the DevOps Diagram"
  type        = string
  default     = "DevopsDiagram"
}