from os import getcwd
from git import Repo

paths = getcwd()
m_repo = Repo(paths)
commit_message = input('Insira o Commit:')

for remote in m_repo.remotes:
    print(f'- {remote.name} {remote.url}')

def git_push():
    try:
        m_repo.git.add(A=True)
        m_repo.git.add(update=True)
        m_repo.index.commit(commit_message)
        origin = m_repo.remote(name='origin')
        origin.push()
    except git.exc.GitCommandError as error:
        print(f'Aconteceu um Erro {error}')

if m_repo.is_dirty(untracked_files=True):
    print('Foram encontradas alterações')
    git_push()
    print('O repositório foi atualizado com Sucesso!')
else:
    print('Não houve alteração!')