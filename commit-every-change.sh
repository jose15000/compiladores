#!/bin/bash

# Verifica se há arquivos modificados
if [[ -z $(git status --porcelain) ]]; then
  echo "Nenhuma modificação encontrada."
  exit 0
fi

# Itera sobre cada arquivo modificado
for file in $(git status --porcelain | grep '^[AM]' | awk '{print $2}'); do
  echo "Adicionando e comitando: $file"

  # Adiciona o arquivo ao staging
  git add "$file"

  # Comita com uma mensagem padrão (substitua conforme necessário)
  git commit -m "Comitando alterações no arquivo $file"
done

echo "Todos os arquivos foram comitados individualmente."
