# mL-project

# need conda environment
```
conda create -p env_name python==3.7 -y
```

# to setup CI CD Pipeline
```
Heroku email:chakrabortytanmay326@gmail.com
Heroku api:af0bf145-8268-42c6-adab-0213aac9563c
heroku name:ml-4regressor-app
```
# build docker image
```
docker build -t <image name>:<tag name> .
```

# to check docker images
```
docker images
```
# run docker 
```
docker run -p 5000:5000 -e PORT=5000 7c60094d6798
```


# data drift
when we data stats will be changed then that called data drift