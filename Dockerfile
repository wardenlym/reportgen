FROM python:3.9-slim-buster
WORKDIR /app

RUN apt-get update -y && \
  apt-get install -y gnupg wget curl unzip --no-install-recommends && \
  wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - && \
  echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list && \
  apt-get update -y && \
  apt-get install -y google-chrome-stable && \
  CHROMEVER=$(google-chrome --product-version | grep -o "[^\.]*\.[^\.]*\.[^\.]*") && \
  DRIVERVER=$(curl -s "https://chromedriver.storage.googleapis.com/LATEST_RELEASE_$CHROMEVER") && \
  wget -q --continue -P /chromedriver "http://chromedriver.storage.googleapis.com/$DRIVERVER/chromedriver_linux64.zip"
  
RUN unzip /chromedriver/chromedriver* -d /chromedriver && \
  ls /chromedriver && \
  chmod 755 /chromedriver/chromedriver && \
  mv /chromedriver/chromedriver /usr/bin/chromedriver

# Update the package list and install chrome
RUN apt-get update -y
RUN apt-get install -y google-chrome-stable

RUN apt install -y fonts-droid-fallback fonts-wqy-zenhei fonts-wqy-microhei fonts-arphic-ukai fonts-arphic-uming

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY __main__.py .
CMD [ "python3", ".", "--host=0.0.0.0"]
