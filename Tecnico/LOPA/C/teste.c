#include <stdio.h>
#include <string.h>

#define MAX_TAREFAS 100
#define TAM_DESCRICAO 100

typedef struct {
    int id;
    char descricao[TAM_DESCRICAO];
    int concluida;
} Tarefa;

void limparBuffer() {
    int c;

    while ((c = getchar()) != '\n' && c != EOF) {
        // Limpa caracteres restantes do buffer
    }
}

void adicionarTarefa(Tarefa tarefas[], int *quantidade, int *proximoId) {
    if (*quantidade >= MAX_TAREFAS) {
        printf("Limite de tarefas atingido.\n");
        return;
    }

    limparBuffer();

    printf("Digite a descricao da tarefa: ");
    fgets(
        tarefas[*quantidade].descricao,
        TAM_DESCRICAO,
        stdin
    );

    tarefas[*quantidade].descricao[
        strcspn(tarefas[*quantidade].descricao, "\n")
    ] = '\0';

    if (strlen(tarefas[*quantidade].descricao) == 0) {
        printf("A descricao nao pode estar vazia.\n");
        return;
    }

    tarefas[*quantidade].id = (*proximoId)++;
    tarefas[*quantidade].concluida = 0;

    (*quantidade)++;

    printf("Tarefa adicionada com sucesso!\n");
}

void listarTarefas(Tarefa tarefas[], int quantidade) {
    if (quantidade == 0) {
        printf("Nenhuma tarefa cadastrada.\n");
        return;
    }

    printf("\n--- Lista de Tarefas ---\n");

    for (int i = 0; i < quantidade; i++) {
        printf(
            "[%c] %d - %s\n",
            tarefas[i].concluida ? 'X' : ' ',
            tarefas[i].id,
            tarefas[i].descricao
        );
    }
}

void concluirTarefa(Tarefa tarefas[], int quantidade) {
    int id;

    printf("Digite o ID da tarefa: ");
    scanf("%d", &id);

    for (int i = 0; i < quantidade; i++) {
        if (tarefas[i].id == id) {
            tarefas[i].concluida = 1;
            printf("Tarefa concluida!\n");
            return;
        }
    }

    printf("Tarefa nao encontrada.\n");
}

void removerTarefa(Tarefa tarefas[], int *quantidade) {
    int id;
    int indice = -1;

    printf("Digite o ID da tarefa: ");
    scanf("%d", &id);

    for (int i = 0; i < *quantidade; i++) {
        if (tarefas[i].id == id) {
            indice = i;
            break;
        }
    }

    if (indice == -1) {
        printf("Tarefa nao encontrada.\n");
        return;
    }

    for (int i = indice; i < *quantidade - 1; i++) {
        tarefas[i] = tarefas[i + 1];
    }

    (*quantidade)--;

    printf("Tarefa removida com sucesso!\n");
}

int main() {
    Tarefa tarefas[MAX_TAREFAS];

    int quantidade = 0;
    int proximoId = 1;
    int opcao;

    do {
        printf("\n===== GERENCIADOR DE TAREFAS =====\n");
        printf("1. Adicionar tarefa\n");
        printf("2. Listar tarefas\n");
        printf("3. Concluir tarefa\n");
        printf("4. Remover tarefa\n");
        printf("0. Sair\n");
        printf("Escolha uma opcao: ");

        scanf("%d", &opcao);

        switch (opcao) {
            case 1:
                adicionarTarefa(tarefas, &quantidade, &proximoId);
                break;

            case 2:
                listarTarefas(tarefas, quantidade);
                break;

            case 3:
                concluirTarefa(tarefas, quantidade);
                break;

            case 4:
                removerTarefa(tarefas, &quantidade);
                break;

            case 0:
                printf("Programa encerrado.\n");
                break;

            default:
                printf("Opcao invalida.\n");
        }

    } while (opcao != 0);

    return 0;
}
