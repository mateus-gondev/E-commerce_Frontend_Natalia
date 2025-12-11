const ORDERS_KEY = "orders";

const orderStore = {
  // Retorna todos os pedidos salvos
  getOrders() {
    const orders = localStorage.getItem(ORDERS_KEY);
    return orders ? JSON.parse(orders) : [];
  },

  // Salva no localStorage
  saveOrders(orders) {
    localStorage.setItem(ORDERS_KEY, JSON.stringify(orders));

    // Dispara evento para atualizar componentes
    window.dispatchEvent(new Event("orders-updated"));
  },

  // Adiciona um novo pedido
  addOrder(order) {
    const orders = this.getOrders();

    const novoPedido = {
      id: Date.now(), // id único baseado no tempo
      date: new Date().toISOString(), // horário do pedido
      ...order // items + total
    };

    orders.push(novoPedido);
    this.saveOrders(orders);

    return novoPedido;
  },

  // Apaga todos os pedidos (caso queira usar)
  clearOrders() {
    localStorage.setItem(ORDERS_KEY, JSON.stringify([]));
    window.dispatchEvent(new Event("orders-updated"));
  }
};

export default orderStore;
