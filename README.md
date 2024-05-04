## Setup Environment (Linux)

### 1. Clone the Repository

```bash
git clone git@github.com:BrandonMagana/MyMusicGenerator.git 
cd MyMusicGenerator
```
### 2. Create and Activate Virtual Environment

```bash
# Install virtualenv if not already installed
sudo apt install python3-venv

# Create a virtual environment
python3 -m venv .venv

# Activate the virtual environment
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Code
You can now run the main script to create a melody.  
```
python3 main.py
```


## Reflexion
Es posible reconocer los patrones repetitivos de la música que nos gusta mediante el uso de tecnología. Por ejemplo podriamos aplicar técnicas de machine learning y así entrenar un modelo utilizando algoritmos especializados así como un dataset de mñusica que contenga el estilo que queramos replicar, y así reconocer y replicar esos patrones para generar música. Esto permitiría al modelo aprender distintos estilos musicales y generar piezas originales siguiendo esas pautas. Sin embargo, es importante tener en cuenta que, aunque el modelo puede aprender a imitar ciertos estilos, sus limitaciones radican en la comprensión más profunda del contexto emocional y la improvisación creativa que a menudo están presentes en la música humana.
