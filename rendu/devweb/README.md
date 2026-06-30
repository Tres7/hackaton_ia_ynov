# TechCorp AI Chat Client

Client web pour interagir avec le modele financier TechCorp.

## Lancer le client en mode developpement

Placez-vous dans le dossier du client :

```bash
cd rendu/devweb
```

Installez les dependances si le dossier `node_modules` n'existe pas encore :

```bash
npm install
```

Lancez le serveur de developpement :

```bash
npm run dev
```

Apres le demarrage, Vite affiche une adresse locale, generalement :

```text
http://localhost:5173
```

Ouvrez cette adresse dans votre navigateur.


## API du modele

Par defaut, le client envoie les requetes vers :

```text
/api/generate
```

En mode developpement, Vite proxifie `/api` vers `https://hardev.eu` via `vite.config.ts`.

Pour utiliser un autre endpoint, creez un fichier `.env` dans `rendu/devweb` :

```env
VITE_TECHCORP_API_URL=http://localhost:11434/api/generate
```

!!IMPORTANT: Cette API sera désactivée le 2 juillet 2026.