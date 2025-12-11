const CART_KEY = "cart";

const cartStore = {
  getCart() {
    const cart = localStorage.getItem(CART_KEY);
    return cart ? JSON.parse(cart) : [];
  },

  saveCart(cart) {
    localStorage.setItem(CART_KEY, JSON.stringify(cart));

    // 🔥 Atualiza o carrinho no componente
    window.dispatchEvent(new Event("cart-updated"));
  },

  add(product) {
    const cart = this.getCart();

    const existente = cart.find(item => item.id === product.id);

    if (existente) {
      existente.quantity += 1;
    } else {
      cart.push({ ...product, quantity: 1 });
    }

    this.saveCart(cart);

    // 🔥 Abre o carrinho ao adicionar produto
    window.dispatchEvent(new Event("open-cart"));
  },

  remove(id) {
    const cart = this.getCart().filter(item => item.id !== id);
    this.saveCart(cart);
  },

  changeQuantity(id, qty) {
    const cart = this.getCart();
    const item = cart.find(item => item.id === id);

    if (!item) return;

    item.quantity = qty <= 0 ? 1 : qty;
    this.saveCart(cart);
  },
};

export default cartStore;
