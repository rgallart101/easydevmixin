# EasyDevMixin Website

This project is a static website built using [Pelican](https://getpelican.com/), a static site generator written in Python. It serves as a blog focused on development topics, including tutorials, tips, and resources for developers, particularly in areas like Python, Django, Magento, and general software development practices.

The site is multilingual, supporting English and Catalan (ca), with content organized in Markdown files under the `content/` directory. Generated output is placed in the `output/` directory.

## Setup Instructions

### Prerequisites
- Python 3.x
- pip (Python package installer)
- Git (for cloning the repository, if applicable)

### Installation
1. Clone or download the project repository to your local machine.

2. Install the required Python packages:
   ```
   pip install -r requirements.txt
   ```

3. (Optional) If you have a virtual environment, activate it before installing dependencies.

### Building the Site
To generate the static HTML files:
```
make html
```

For production builds (with optimized settings):
```
make publish
```

### Serving Locally
To serve the site locally for development:
```
make serve
```
This will start a local server at `http://localhost:8000` (or the port specified in the Makefile).

For development with automatic regeneration on file changes:
```
make devserver
```

### Publishing
To upload the site via SSH, SFTP, or rsync, configure the required environment variables. Create a `.env` file in the project root with the following variables:

- `ENV_SSH_HOST`: The SSH host (e.g., your server IP or domain)
- `ENV_SSH_PORT`: The SSH port (default is 22)
- `ENV_SSH_USER`: The SSH username
- `ENV_SSH_TARGET_DIR`: The target directory on the server

Example `.env` file:
```
ENV_SSH_HOST=example.com
ENV_SSH_PORT=22
ENV_SSH_USER=username
ENV_SSH_TARGET_DIR=/var/www/html
```

Then run:
- SSH: `make ssh_upload`
- SFTP: `make sftp_upload`
- Rsync: `make rsync_upload`

### Configuration
- Main configuration: `pelicanconf.py`
- Production configuration: `publishconf.py`
- Content is in `content/` (Markdown files)
- Themes and plugins are in `output/theme/` and `plugins/`

### Additional Commands
- Clean generated files: `make clean`
- Regenerate on changes: `make regenerate`
- View help: `make help`

For more details, refer to the [Pelican documentation](https://docs.getpelican.com/).
