# diagram.py

import os
from diagrams import Diagram, Cluster, Edge
from diagrams.azure.compute import VMLinux
from diagrams.custom import Custom
from diagrams.generic.blank import Blank
from diagrams.azure.devops import Artifacts, Devops, Pipelines, Repos, TestPlans

graph = {
    "fontsize": "45",
    "bgcolor": "transparent",
}

big_cluster_graph = {
    "fontsize": "30",
    "bgcolor": "lightblue",
}

cluster_graph_blue = {
    "fontsize": "20",
    "bgcolor": "lightblue"
}

cluster_graph_none = {
    "fontsize": "20",
}

workingDirectory = os.path.dirname(os.path.abspath(__file__))

def main():
    with Diagram("Build System Design - Kevin", show=False, filename=workingDirectory + "/overview_diagram", direction="LR", graph_attr=graph):

      ### GITHUB DEPOT CLUSTERS ###
      with Cluster("SCM - GitHub Depot Contents", graph_attr=cluster_graph_blue):
        jenkins_file = new_jenkins_img("Jenkins File")
        docker_file = new_docker_img("File")
        github_cluster = [Custom("Diagram", "") \
            - jenkins_file \
            - new_terraform_img("Terraform Config") \
            - docker_file \
            - new_ansible_img("Ansible Script")]        
      
      img_github = Custom("GitHub Depot", workingDirectory + "/resources/github/mark_png/GitHub-Mark-120px-plus.png")
      
      ### BIG CLUSTER GRAPH ###
      with Cluster("Azure Cloud", graph_attr=big_cluster_graph):
      
          ### DOCKER CONTAINERS CLUSTERS###
          with Cluster("Docker Cluster", graph_attr=cluster_graph_none):
            docker_img_1 = new_docker_img("HTML Server")
            docker_img_1 >> Custom("Diagram Hosted :9999", "")

            docker_img_3 = new_docker_img("Container")
            docker_img_3 >> Edge(label="create") >>Artifacts("Image") >> Edge(label="push") >> new_docker_img("Repository")
            docker_containers_cluster = [docker_img_1, docker_img_3]
          
          ### JENKINS CLUSTERS ###
          with Cluster("Jenkins Nodes", graph_attr=cluster_graph_none):
            jenkins_server = VMLinux("Jenkins Server")
            jenkins_agent = VMLinux("Jenkins Agent")
            jenkins_cluster = [jenkins_server, jenkins_agent]
          
          docker_img_2 = new_docker_img("Container")
          docker_img_2 >> Edge(label="execute") >>Pipelines("Jobs") >> Edge(label="validate") >> TestPlans("Tests")
          
          img_terraform = new_terraform_img("Terraform")
          
          jenkins_agent \
            >> Edge(label="running") \
            >> docker_img_2
          
          jenkins_agent \
            >> Edge(label="call") \
            >> img_terraform 
  
          img_terraform >> docker_img_1
          img_terraform >> docker_img_3

      github_cluster \
        >> img_github \
        >> Edge(label="commit trigger") \
        >> Repos("Multibranch Pipeline") \
        >> Edge(label="sync") \
        >> jenkins_cluster
        
      jenkins_file >> \
        Edge(label="define") >> \
        [TestPlans("Validation Tests"), Pipelines("Jobs")]
        
      new_ansible_img("Ansible Script") >> Edge(label="configure") >> jenkins_agent
    
    return 0
      
def new_terraform_img(text):
    return Custom(text, workingDirectory + "/resources/terraform/Terraform_VerticalLogo_Color_RGB.png")

def new_docker_img(text):
    return Custom(text, workingDirectory + "/resources/docker/vertical-logo-monochromatic.png")  
    
def new_jenkins_img(text):
    return Custom(text, workingDirectory + "/resources/jenkins/128x128/logo.png")

def new_ansible_img(text):
    return Custom(text, workingDirectory + "/resources/ansible/Ansible-Mark-RGB_Pool.png")
    
if __name__ == "__main__":
    main()