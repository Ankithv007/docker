### my simple project with the help of chat gpt 
#### ChatGPT helped me to develop the Django code, which I then used to build the Docker project. 
#### tree view of the project 
```
mywebsite/
├── Dockerfile
├── requirements.txt
├── manage.py
├── db.sqlite3  # Generated after migrations
├── home/
│   ├── __init__.py
│   ├── urls.py
│   ├── views.py
│   └── templates/
│       └── home/
│           └── index.html
├── mywebsite/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py (If the EC2 instance does not have an Elastic IP address, we need to change its public IP address every time it is stopped and started.)
│   ├── urls.py
│   └── wsgi.py
└── templates/  # General templates directory (optional)
```

###  Build the Docker Image (. for present directory if its not we have provide the path -f (file* / folder) -t (tag) tag to find the image easily
##### . (dot) at the end specifies the build context, which is typically the current directory. Adjust this if your context is different.

```
docker build -t my-django-app .
```
```
docker build -f /path/to/Dockerfile -t my-image-name .
```
### Verify the Image
```
docker images
```
##### You should see my-django-app in the list of images.

### Run a Container from the Image (look into Dockerfile  it should be the same as in the Dockerfile)

```
docker run -d -p 8000:8000 --name my-django-app-container my-django-app
```
- -d runs the container in detached mode (in the background).
- -p 8000:8000 maps port 8000 of the container to port 8000 on the host
- --name my-django-app-container gives the container a name (my-django-app-container)
- my-django-app is the name of the image you created.

  ##### After building and running your Docker container, you typically need to perform the following additional steps to ensure your application is fully set up and accessible:

  ### Apply Migrations
  ###### If your application requires database migrations (e.g., Django projects), you need to apply them
  ```
  docker exec -it my-django-app-container python manage.py migrate

  ```
  ### don't forget to change the sg group both http (80)  and port 8000 in sg
  ### Create a Superuser
   ###### Create a Superuser
  ```
  docker exec -it my-django-app-container python manage.py createsuperuser
  
  ```
##### Follow the prompts to enter the username, email, and password

```
https://chatgpt.com/share/889cea53-fc3e-4300-8beb-d0925edf096c
```
