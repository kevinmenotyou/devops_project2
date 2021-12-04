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
  count = "${var.local_registry_spawned == true ? 1 : 0}"
}

resource "docker_container" "devops-diagram" {
  image = docker_image.devops-diagram[0].latest
  name  = var.devops_diagram_container_name
  ports {
    internal = 80
    external = 9000
  }
  count = "${var.local_registry_spawned == true ? 1 : 0}"
}