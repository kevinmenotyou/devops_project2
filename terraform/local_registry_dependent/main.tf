terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 2.7"
    }
  }
}

provider "docker" {
  registry_auth {
    address     = "localhost:5000"
  }
}

resource "docker_image" "devops-diagram" {
  name         = "devops-diagram"
  keep_locally = false
}

resource "docker_container" "devops-diagram" {
  image = docker_image.devops-diagram.latest
  name  = var.devops_diagram_container_name
  ports {
    internal = 80
    external = 9000
  }
}