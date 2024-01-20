# 基于 Python 镜像
FROM python:3.9.17-slim as python-base

ENV PYTHONUNBUFFERED=1 \
    # pip
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    \
    # Poetry的版本
    # https://python-poetry.org/docs/configuration/#using-environment-variables
    POETRY_VERSION=1.7.1 \
    # Poetry的安装位置
    POETRY_HOME="/opt/poetry" \
    # 没有用户互动
    POETRY_NO_INTERACTION=1 \
    # 不要自动创建新的虚拟环境，我们只让Python和Poetry用待会我们自己创建好的，
    # 无论是构建还是运行时都是如此。
    POETRY_VIRTUALENVS_CREATE=false \
    \
    # 项目依赖和虚拟环境最后会放在这里
    VIRTUAL_ENV="/venv"

# 让系统能够找到Poetry和VIRTUAL_ENV
ENV PATH="$POETRY_HOME/bin:$VIRTUAL_ENV/bin:$PATH"

RUN python -m venv $VIRTUAL_ENV

# 设定工作目录
WORKDIR /app
ENV PYTHONPATH="/app:$PYTHONPATH"

# 国内镜像源
RUN sed -i 's/deb.debian.org/mirrors.cloud.tencent.com/g' /etc/apt/sources.list.d/debian.sources && \
    pip config set global.index-url https://mirrors.cloud.tencent.com/pypi/simple

################################
# BUILDER-BASE
# 安装和编译依赖
################################
FROM python-base as builder-base
RUN apt-get update && \
    apt-get install -y \
    apt-transport-https \
    gnupg \
    ca-certificates \
    build-essential \
    git \
    nano \
    curl

# 将 Poetry.lock 和 pyproject.toml 文件复制到容器中
COPY poetry.lock pyproject.toml /app/

# 安装 Poetry 工具
RUN --mount=type=cache,target=/root/.cache \
    curl -sSL https://install.python-poetry.org | python -

# 使 Poetry 的可执行文件生效
ENV PATH "/root/.poetry/bin:$PATH"

# 安装依赖项并清除构建时缓存
RUN poetry install --no-root && rm -rf /root/.cache

# 将程序代码复制到容器中
COPY . /app

# 设定程序入口
EXPOSE 8080
CMD ["python", "exam/server_client.py"]