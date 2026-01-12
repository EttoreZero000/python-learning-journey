FROM python:3.12-slim

# crear usuario sin privilegios
ARG USERNAME=appuser
ARG USER_UID=1000
ARG USER_GID=$USER_UID

RUN groupadd --gid $USER_GID $USERNAME \
    && useradd --uid $USER_UID --gid $USER_GID -m $USERNAME

WORKDIR /app

# instalar deps del sistema (opcional)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# instalar pip deps como root (normal en docker)
COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir --upgrade pip && pip install -r /tmp/requirements.txt

# copiar y dar permisos
COPY . .
RUN chown -R $USERNAME:$USERNAME /app

# cambiar a usuario no root
USER $USERNAME
