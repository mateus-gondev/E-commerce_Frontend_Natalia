<template>
    <!--VALORES FICTICIOS-->
    <div class="container-pedidos">
        <h3 class="titulo">Lista de Pedidos</h3>

        <table class="tabela-pedidos table-striped table-hover align-middle">
            <thead class="cont-coluna">
                <tr class="coluna">
                    <th>Nome do Cliente</th>
                    <th>Endereço</th>
                    <th>Data do Pedido</th>
                    <th>Valor Total</th>
                    <th>Status</th>
                    <th>Ações</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>Maria Oliveira</td>
                    <td>Rua das Flores, 123</td>
                    <td>2025-11-02</td>
                    <td>R$ 320,00</td>
                    <td><span class="status concluido">Concluído</span></td>
                    <td>
                        <button class="btn editar">Editar</button>
                        <button class="btn remover">Remover</button>
                    </td>
                </tr>
                <tr>
                    <td>João Santos</td>
                    <td>Av. Paulista, 500</td>
                    <td>2025-10-29</td>
                    <td>R$ 185,50</td>
                    <td><span class="status andamento">Em andamento</span></td>
                    <td>
                        <button class="btn editar">Editar</button>
                        <button class="btn remover">Remover</button>
                    </td>
                </tr>
                <tr>
                    <td>Ana Costa</td>
                    <td>Rua Bela Vista, 77</td>
                    <td>2025-10-15</td>
                    <td>R$ 512,90</td>
                    <td><span class="status cancelado">Cancelado</span></td>
                    <td>
                        <button class="btn editar">Editar</button>
                        <button class="btn remover">Remover</button>
                    </td>
                </tr>
            </tbody>
        </table>
    </div>
</template>

<script>
export default {
    name: "AdmPedidos"
}
</script>

<style scoped>
:root {
    --preto: #141414;
    --azul: #4e31d0;
    --branco: #ffffff;
    --cinza: #f6f6f6;
    --texto: #1a1a1a;
}
.cont-coluna{
    background-color: var(--azul);
    color: var(--branco);
}

.container-pedidos {
    margin: 50px auto;
    width: 100%;
    background-color: #f6f6f6;
    color: var(--texto);
    padding: 30px;
    border-radius: 12px;
    box-shadow: 0 4px 25px rgba(0, 0, 0, 0.1);

}

.titulo {
    text-align: center;
    color: var(--preto);
    margin-bottom: 25px;
    font-weight: 700;
    letter-spacing: 1px;
}

.tabela-pedidos {
    width: 100%;
    border-collapse: collapse;
    border-radius: 8px;
    overflow: hidden;
}

.tabela-pedidos thead {
    background-color: var(--azul);
    color: #f6f6f6;
    text-transform: uppercase;
    font-size: 0.9rem;
}

.tabela-pedidos th,
.tabela-pedidos td {
    padding: 12px 15px;
    text-align: center;
}

.tabela-pedidos tbody tr:nth-child(even) {
    background-color: #f6f6f6;
}

.tabela-pedidos tbody tr:hover {
    background-color: rgba(78, 49, 208, 0.1);
    transition: background-color 0.3s ease;
}

.status {
    padding: 6px 12px;
    border-radius: 5px;
    font-weight: 600;
    font-size: 0.85rem;
}

.status.concluido {
    background-color: #53f579;
    color: #141414;
}

.status.andamento {
    background-color:  #522cff;
    color: #f6f6f6;
}

.status.cancelado {
    background-color: #dc3545;
    color: #f6f6f6;
}

.btn {
    padding: 6px 12px;
    border: none;
    border-radius: 6px;
    font-size: 0.85rem;
    font-weight: 600;
    cursor: pointer;
    transition: 0.3s;
    margin-right: 5px;
}

.btn.editar,
.btn.remover {
    background-color: var(--azul);
    color: var(--branco);
}

.btn.editar:hover {
    background-color: #3a25b0;
    color: #f6f6f6;
}

.btn.remover:hover {
    background-color: #b11f30;
    color: #f6f6f6;
}
</style>
