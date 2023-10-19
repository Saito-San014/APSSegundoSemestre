import subprocess

# O comando a ser executado (instalação de um pacote)
command = {
    "rsa" : ["pip", "install", "rsa"],
    "cryptography" : ["pip", "install", "cryptography"]
    }
def config(lib):
    # Execute o comando pip
    try:
        subprocess.check_call(command[lib])
        print("Pacote instalado com sucesso.")
    except subprocess.CalledProcessError as e:
        print(f"Erro ao instalar o pacote: {e}") 
