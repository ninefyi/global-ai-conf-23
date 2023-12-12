# Install Node.js version 18
apt-get update \
    && apt-get install -y curl \
    && apt-get -y autoclean

# install nvm
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash
export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"  # This loads nvm
[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"

# install node and npm
NODE_VERSION=18.19.0
nvm install $NODE_VERSION \
    && nvm alias default $NODE_VERSION \
    && nvm use default

cd ./fastapi && uvicorn main:app --reload --host=0.0.0.0 --port=8000