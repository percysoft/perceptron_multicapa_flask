FROM python:3
RUN mkdir /code
COPY . /code/
WORKDIR /code/
RUN pip install --upgrade pip && \
    pip install flask && \
    pip3 install pandas && \
    pip install -U scikit-learn scipy matplotlib && \
    pip3 install numpy
EXPOSE 5000
CMD ["python", "main.py"]