variable "project_id" {
  default = "todo-er"
}

resource "google_compute_network" "tfnetwork" {
  name                    = "tfnetwork"
  project                 = var.project_id
  auto_create_subnetworks = false
}

resource "google_compute_subnetwork" "subnet-europe-west1" {
  project       = var.project_id
  name          = "subnet-europe-west1"
  network       = google_compute_network.tfnetwork.self_link
  ip_cidr_range = "10.2.0.0/16"
  region        = "europe-west1"
}

resource "google_compute_firewall" "tfnetwork-allow-http-ssh-icmp" {
  project = var.project_id
  name    = "tfnetwork-allow-http-ssh-icmp"
  network = google_compute_network.tfnetwork.self_link
  allow {
    protocol = "tcp"
    ports    = ["22", "80", "8080"]
  }
  allow {
    protocol = "icmp"
  }
}

resource "google_compute_instance" "vm_instance" {
  project                 = var.project_id
  name                    = "apache-server"
  zone                    = "europe-west1-d"
  machine_type            = "n1-standard-1"
  metadata_startup_script = file("./startup.sh")
  boot_disk {
    initialize_params {
      image = "debian-cloud/debian-9"
    }
  }
  network_interface {
    network    = google_compute_network.tfnetwork.self_link
    subnetwork = google_compute_subnetwork.subnet-europe-west1.self_link
    access_config {

    }
  }
}

output "external_ip" {
  value = google_compute_instance.vm_instance.network_interface.0.access_config.0.nat_ip
}


