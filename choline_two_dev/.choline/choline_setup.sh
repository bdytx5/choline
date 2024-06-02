#!/bin/bash
echo "starting choline setup"
# Download and install ollama
sudo curl -L https://ollama.ai/download/ollama-linux-amd64 -o /usr/bin/ollama
sudo chmod +x /usr/bin/ollama

# # Ensure no previous instance is running
sudo pkill -f 'ollama serve'
nohup /usr/bin/ollama serve > /var/log/ollama_serve.log 2>&1 &

  # Give some time for ollama to start serving
  # Wait for ollama serve to be ready
  echo "Waiting for ollama serve to be ready..."
  while ! grep -q "Nvidia GPU detected" /var/log/ollama_serve.log; do
    sleep 5 # Check every 5 seconds
  done
  echo "ollama serve is ready."


# Start the pull operation in the background
/usr/bin/ollama pull mistral > /var/log/ollama_pull.log 2>&1 &

# Wait for the pull to complete successfully
echo "Waiting for ollama to pull the model..."
while ! grep -q "success" /var/log/ollama_pull.log; do
  sleep 10 # Check every 10 seconds
done

echo "Model pull completed successfully."

# Optionally, run a model command if needed
# /usr/bin/ollama run mistral & # Assuming there's a command to run the model

echo "Setup complete. Check /var/log/ollama_pull.log for pull details."
sudo apt upgrade
sudo apt install vim -y
sudo apt install python3 -y
sudo apt install python3-pip -y
pip install Flask==2.3.2 || pip3 install Flask==2.3.2 -y
pip install watchdog || pip3 install watchdog -y
git clone https://github.com/bdytx5/choline_templates.git
sudo python3 choline_templates/jank_ssh_api.py > ~/.choline/chat_api_out.txt 2>&1 &
sleep 10 
sudo curl -X POST http://127.0.0.1:5000/predict -H "Content-Type: application/json" -d '{"prompt": "hello"}' 