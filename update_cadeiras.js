const fs = require('fs');
let code = fs.readFileSync('products.js', 'utf8');

const cadeiras = [
  { id: 'cadeira-charly', name: 'Cadeira Charly', desc: 'Cadeira estofada. Pés disponíveis em lacado (branco, preto, gris e cinza), verniz (wengué, cerejeira, faia e freixo natura).' },
  { id: 'cadeira-perola', name: 'Cadeira Pérola', desc: 'Cadeira estofada. Pés disponíveis em lacado (branco, preto, gris e cinza) ou verniz (wengué, cerejeira e faia). Opção de copo metálico.' },
  { id: 'cadeira-moon', name: 'Cadeira Moon', desc: 'Cadeira estofada. Pés disponíveis em lacado (branco, preto, gris e cinza) ou verniz (wengué, cerejeira e faia). Opção de copo metálico.' },
  { id: 'cadeira-sea', name: 'Cadeira Sea', desc: 'Cadeira estofada. Pés disponíveis em lacado (branco, preto, gris e cinza) ou verniz (wengué, cerejeira e faia).' },
  { id: 'cadeira-sky', name: 'Cadeira Sky', desc: 'Cadeira estofada. Pés disponíveis em lacado (branco, preto, gris e cinza) ou verniz (wengué, cerejeira e faia).' },
  { id: 'cadeira-bona', name: 'Cadeira Bona', desc: 'Cadeira estofada. Pés disponíveis em lacado (branco, preto, gris e cinza) ou verniz (wengué, cerejeira, faia e pinho mel).' },
  { id: 'cadeira-florenca', name: 'Cadeira Florença', desc: 'Cadeira estofada. Pés disponíveis em lacado (branco, preto, gris e cinza) ou verniz (wengué, cerejeira e pinho mel).' },
  { id: 'cadeira-saturno', name: 'Cadeira Saturno', desc: 'Cadeira estofada. Pés disponíveis em lacado (branco, preto, gris e cinza) ou verniz (wengué, cerejeira, faia e pinho mel).' },
  { id: 'cadeira-paris', name: 'Cadeira Paris', desc: 'Cadeira estofada. Pés disponíveis em lacado (branco, preto, gris e cinza) ou verniz (wengué, cerejeira e pinho mel).' },
  { id: 'cadeira-sagres', name: 'Cadeira Sagres', desc: 'Cadeira estofada. Pés disponíveis em lacado (branco, preto, gris e cinza) ou verniz (wengué, cerejeira, faia e pinho mel).' },
  { id: 'cadeira-madrid', name: 'Cadeira Madrid', desc: 'Cadeira estofada. Pés disponíveis em lacado (branco, preto, gris e cinza) ou verniz (wengué, cerejeira e pinho mel).' },
  { id: 'cadeira-utopia', name: 'Cadeira Utopia', desc: 'Costa e assento estofado. Acabamentos disponíveis em lacado (branco, preto, gris e cinza) ou verniz (wengué, cerejeira e faia).' },
  { id: 'cadeira-milao', name: 'Cadeira Milão', desc: 'Costa e assento estofado. Acabamentos disponíveis em lacado (branco, preto, gris e cinza) ou verniz (wengué, cerejeira e faia).' },
  { id: 'cadeira-serpa', name: 'Cadeira Serpa', desc: 'Assento estofado ou madeira. Acabamentos disponíveis em lacado (branco, preto, gris e cinza) ou verniz (wengué, cerejeira e pinho mel).' },
  { id: 'cadeira-chiado', name: 'Cadeira Chiado', desc: 'Assento estofado. Acabamentos disponíveis em lacado (branco, preto, gris e cinza) ou verniz (wengué, cerejeira e pinho mel).' },
  { id: 'cadeira-viena', name: 'Cadeira Viena', desc: 'Assento estofado. Acabamentos disponíveis em lacado (branco, preto, gris e cinza) ou verniz (wengué, cerejeira e faia).' },
  { id: 'cadeira-rio', name: 'Cadeira Rio', desc: 'Assento estofado. Pés disponíveis em lacado (branco, preto, gris e cinza) ou verniz (wengué, cerejeira e pinho mel).' }
];

let added = 0;
// We will inject them right before the closing brace of the main object.
// The main object is `const adilProducts = { ... };`
let insertionIndex = code.lastIndexOf('};');

let newStr = "";
for (let c of cadeiras) {
  if (!code.includes(c.id)) {
    newStr += `,
  "${c.id}": {
    "id": "${c.id}",
    "name": "${c.name}",
    "price": 0.00,
    "url": "complementos.html",
    "description": "${c.desc}",
    "custom1_name": "Tecido / Cor",
    "custom1_options": "A escolher em loja",
    "custom2_name": "",
    "custom2_options": "",
    "image": "images/logo.png"
  }`;
    added++;
  }
}

if (added > 0) {
  code = code.substring(0, insertionIndex) + newStr + "\n" + code.substring(insertionIndex);
  fs.writeFileSync('products.js', code);
  console.log(`Added ${added} Cadeiras.`);
} else {
  console.log('No Cadeiras to add.');
}
