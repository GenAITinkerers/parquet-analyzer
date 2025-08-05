## 🧰 Docker Compose - Common Commands

Below is a list of commonly used `docker-compose` commands to manage multi-container applications.

### 📦 Basic Commands

| Command | Description |
|---------|-------------|
| `docker-compose up` | Builds, (re)creates, starts, and attaches to containers for a service. |
| `docker-compose up -d` | Runs containers in the background (detached mode). |
| `docker-compose down` | Stops and removes all containers, networks, volumes, and images created by `up`. |
| `docker-compose build` | Builds or rebuilds services defined in the Compose file. |
| `docker-compose start` | Starts existing containers for a service. |
| `docker-compose stop` | Stops running containers without removing them. |
| `docker-compose restart` | Restarts running containers. |
| `docker-compose ps` | Lists all containers managed by the current Compose file. |
| `docker-compose logs` | Shows logs for all services. |
| `docker-compose logs -f` | Follows log output (like `tail -f`). |

### 🛠️ Advanced Commands

| Command | Description |
|---------|-------------|
| `docker-compose exec <service> <command>` | Runs a command in a running container (e.g., `docker-compose exec web bash`). |
| `docker-compose run <service> <command>` | Runs a one-off command (starts a new container). |
| `docker-compose config` | Validates and shows the full configuration, including overrides. |
| `docker-compose top` | Displays the running processes of services. |
| `docker-compose pull` | Pulls service images from Docker Hub. |
| `docker-compose push` | Pushes built images to Docker Hub. |
| `docker-compose version` | Shows the version of Compose. |

---

### 🔄 Useful Combinations

```bash
# Build and start services
docker-compose up --build

# Stop, remove, and clean everything
docker-compose down --volumes --remove-orphans

# Rebuild a single service
docker-compose build <service-name>

# Enter container's shell
docker-compose exec <service-name> /bin/bash
