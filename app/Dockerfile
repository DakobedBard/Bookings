FROM  continuumio/anaconda3
WORKDIR /usr/src/app
run apt-get update && apt-get install -y netcat
# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /usr/src/app/requirements.txt

RUN apt-get update
RUN apt-get install vim
RUN pip install -r requirements.txt

#
RUN pip install --upgrade pip
# run conda install -c conda-forge librosa
run pip install djangorestframework-jwt
run pip install djangorestframework_simplejwt
run pip install django-rest-auth
run pip install django-rest-auth[with_social]
run pip install django-cors-headers
run pip install django-storages
run pip install boto3

run pip install djangorestframework

COPY ./entrypoint.sh /usr/src/app/entrypoint.sh
# # copy project
 COPY . /usr/src/app/
#
# # run entrypoint.sh
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
