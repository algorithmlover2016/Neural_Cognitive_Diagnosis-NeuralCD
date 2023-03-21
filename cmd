docker run -it  ubuntu:20.04 /bin/bash
apt-get update && apt-get install git vim curl wget
apt install software-properties-common
add-apt-repository ppa:deadsnakes/ppa
apt update && apt install python3.6
rm -rf /usr/bin/python3 && ln -s /usr/bin/python3.6 /usr/bin/python3
rm -rf /usr/bin/python && ln -s /usr/bin/python3.6 /usr/bin/python
apt install python3-pip
apt-get update && apt-get install python3-pip
apt-get install python3.6-distutils
pip install torch===1.0.1 -f https://download.pytorch.org/whl/torch_stable.html
pip install xlrd
pip install pandas
pip3 install -U scikit-learn
 
grep 'user_id' --col ./log_data.json.ori | awk -F '[:,]' '{print $(NF - 1)}' | sort -n | uniq > log.txt
grep 'user_id' --col NeuralCD.json | awk -F '[:,]' '{print $(NF - 1)}' | sort -n | uniq > log.txt
grep -nr 'log_num' --col ./log_data.json | awk '{print$NF}' | sort |uniq
 
 
git clone https://github.com/bigdata-ustc/Neural_Cognitive_Diagnosis-NeuralCD.git
cd Neural_Cognitive_Diagnosis-NeuralCD/
 
cd data ; mv log_data.json log_data.json.ori ; cd ../
python transform_data.py ; cd data; mv trans.json log_data.json; cd ../
python divide_data.py
python train.py cpu 2
