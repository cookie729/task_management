FROM node:16-slim
WORKDIR /app
# WORKDIR /app/task_vue
RUN apt-get update -qq && yarn global add @vue/cli

# # RUN groupadd -g 1000 user
# # RUN useradd -u 1000 -g 1000 -s /bin/bash -m user
COPY .. :
RUN yarn
CMD ["yarn", "dev", "--port", "3000"]
