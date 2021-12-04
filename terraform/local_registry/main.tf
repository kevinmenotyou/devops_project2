terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 2.7"
    }
  }
}

provider "docker" {
}

resource "docker_image" "registry" {
  name         = "registry"
  keep_locally = false
}

resource "docker_container" "registry" {
  image = docker_image.registry.latest
  name  = var.registry_container_name
  ports {
    internal = 5000
    external = 5000
  }
}