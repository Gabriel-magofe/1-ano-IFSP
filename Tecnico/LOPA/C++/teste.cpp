#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <limits>

using namespace std;

class Tarefa {
private:
    int id;
    string descricao;
    bool concluida;

public:
    Tarefa(int id, const string& descricao)
        : id(id), descricao(descricao), concluida(false) {}

    int getId() const {
        return id;
    }

    string getDescricao() const {
        return descricao;
    }

    bool isConcluida() const {
        return concluida;
    }

    void concluir() {
        concluida = true;
    }

    void exibir() const {
        cout << "[" << (concluida ? "X" : " ") << "] "
             << id << " - " << descricao << endl;
    }
};

class GerenciadorTarefas {
private:
    vector<Tarefa> tarefas;
    int proximoId = 1;

public:
    void adicionarTarefa() {
        string descricao;

        cin.ignore(numeric_limits<streamsize>::max(), '\n');

        cout << "Digite a descricao da tarefa: ";
        getline(cin, descricao);

        if (descricao.empty()) {
            cout << "A descricao nao pode estar vazia.\n";
            return;
        }

        tarefas.emplace_back(proximoId++, descricao);
        cout << "Tarefa adicionada com sucesso!\n";
    }

    void listarTarefas() const {
        if (tarefas.empty()) {
            cout << "Nenhuma tarefa cadastrada.\n";
            return;
        }

        cout << "\n--- Lista de Tarefas ---\n";

        for (const Tarefa& tarefa : tarefas) {
            tarefa.exibir();
        }
    }

    void concluirTarefa() {
        int id;

        cout << "Digite o ID da tarefa: ";
        cin >> id;

        for (Tarefa& tarefa : tarefas) {
            if (tarefa.getId() == id) {
                tarefa.concluir();
                cout << "Tarefa concluida!\n";
                return;
            }
        }

        cout << "Tarefa nao encontrada.\n";
    }

    void removerTarefa() {
        int id;

        cout << "Digite o ID da tarefa: ";
        cin >> id;

        auto it = remove_if(
            tarefas.begin(),
            tarefas.end(),
            [id](const Tarefa& tarefa) {
                return tarefa.getId() == id;
            }
        );

        if (it != tarefas.end()) {
            tarefas.erase(it, tarefas.end());
            cout << "Tarefa removida com sucesso!\n";
        } else {
            cout << "Tarefa nao encontrada.\n";
        }
    }

    void executar() {
        int opcao;

        do {
            cout << "\n===== GERENCIADOR DE TAREFAS =====\n";
            cout << "1. Adicionar tarefa\n";
            cout << "2. Listar tarefas\n";
            cout << "3. Concluir tarefa\n";
            cout << "4. Remover tarefa\n";
            cout << "0. Sair\n";
            cout << "Escolha uma opcao: ";
            cin >> opcao;

            switch (opcao) {
                case 1:
                    adicionarTarefa();
                    break;

                case 2:
                    listarTarefas();
                    break;

                case 3:
                    concluirTarefa();
                    break;

                case 4:
                    removerTarefa();
                    break;

                case 0:
                    cout << "Programa encerrado.\n";
                    break;

                default:
                    cout << "Opcao invalida.\n";
            }

        } while (opcao != 0);
    }
};

int main() {
    GerenciadorTarefas gerenciador;
    gerenciador.executar();

    return 0;
}
