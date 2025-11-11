<!--O Form é para criar-editar-remover pelo painel administrativo.-->
<template>
  <div class="adm-layout">
    <AdmNavbar />
    <main class="adm-content">
      <div class="form-container">
        <h1>{{ modoEdicao ? "Editar Usuário" : "Cadastrar Novo Usuário" }}</h1>

        <form @submit.prevent="enviar">
          <div class="form-group">
            <label>Nome</label>
            <input v-model="formData.name" type="text" placeholder="Digite o nome" required />
          </div>

          <div class="form-group">
            <label>Email</label>
            <input v-model="formData.email" type="email" placeholder="Digite o email" required />
          </div>

          <div class="form-group">
            <label>Cargo</label>
            <select v-model="formData.cargo" required>
              <option value="administrador">Administrador</option>
              <option value="funcionario">Funcionário</option>
              <option value="cliente">Cliente</option>
            </select>
          </div>

          <div class="form-group" v-if="!modoEdicao">
            <label>Senha</label>
            <input v-model="formData.password" type="password" placeholder="Digite a senha" required />
          </div>

          <div class="acoes">
            <button type="submit" class="btn-save">{{ modoEdicao ? 'Salvar' : 'Cadastrar' }}</button>
            <button type="button" class="btn-cancel" @click="voltar">Cancelar</button>
          </div>
        </form>
      </div>
    </main>
  </div>
</template>

<script>
import api from "@/services/api";
import AdmNavbar from "../../components/Adm/AdmNavbar.vue";

export default {
  name: "AdmForm",
  components: { AdmNavbar },
  data() {
    return {
      formData: { name: "", email: "", password: "", cargo: "cliente" },
      modoEdicao: false,
      idUsuario: null,
    };
  },
  async mounted() {
    // Aqui verifica se veio um ID na rota para edição
    this.idUsuario = this.$route.params.id;
    if (this.idUsuario) {
      this.modoEdicao = true;
      const res = await api.get(`/users/${this.idUsuario}`);
      this.formData = res.data;
    }
  },
  methods: {
    async enviar() {
      try {
        if (this.modoEdicao) {
          await api.put(`/users/${this.idUsuario}`, this.formData);
          alert("Usuário atualizado com sucesso!");
        } else {
          await api.post("/users", this.formData);
          alert("Usuário cadastrado com sucesso!");
        }
        this.voltar();
      } catch (error) {
        alert(error.response?.data?.error || "Erro ao salvar usuário.");
      }
    },
    voltar() {
      this.$router.push("/adm/usuario");
    },
  },
};
</script>

<style scoped>
.form-container {
  background: #fff;
  border-radius: 12px;
  padding: 2rem;
  max-width: 600px;
  margin: 2rem auto;
  box-shadow: 0 2px 10px rgba(0,0,0,0.1);
}

.form-group {
  margin-bottom: 1.2rem;
}

label {
  display: block;
  font-weight: 600;
  margin-bottom: 0.5rem;
}

input, select {
  width: 100%;
  padding: 0.6rem;
  border: 1px solid #ddd;
  border-radius: 8px;
  font-size: 1rem;
}

.acoes {
  display: flex;
  justify-content: space-between;
  margin-top: 1.5rem;
}

.btn-save {
  background-color: #2c3e50;
  color: white;
  padding: 0.6rem 1.2rem;
  border: none;
  border-radius: 8px;
  cursor: pointer;
}

.btn-save:hover {
  background-color: #34495e;
}

.btn-cancel {
  background-color: #ddd;
  color: #333;
  padding: 0.6rem 1.2rem;
  border: none;
  border-radius: 8px;
  cursor: pointer;
}

.btn-cancel:hover {
  background-color: #bbb;
}
</style>
