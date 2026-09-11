const fs = require('fs');

function getCategoryQuartos(name) {
    name = name.toLowerCase();
    if (name.includes('mesa') && name.includes('cabeceira')) return 'mesasCabeceira';
    if (name.includes('cabeceira')) return 'cabeceiras';
    if (name.includes('cama')) return 'camas';
    if (name.includes('cómoda') || name.includes('comoda')) return 'comodas';
    if (name.includes('camiseiro')) return 'camiseiros';
    if (name.includes('sommier')) return 'sommiers';
    return 'all';
}

function getCategorySalas(name) {
    name = name.toLowerCase();
    if (name.includes('sofá') || name.includes('sofa')) return 'sofas';
    if (name.includes('cadeirão') || name.includes('cadeirao') || name.includes('poltrona')) return 'cadeiroes';
    if (name.includes('mesa') || name.includes('cadeira') || name.includes('banqueta') || name.includes('banco')) return 'mesasEcadeiras';
    if (name.includes('móvel') || name.includes('movel') || name.includes('aparador') || name.includes('estante') || name.includes('vitrine') || name.includes('sapateira') || name.includes('secretária') || name.includes('secretaria') || name.includes('base tv') || name.includes('prateleira')) return 'moveis';
    return 'all';
}

function getCategoryColchoes(name) {
    name = name.toLowerCase();
    if (name.includes('colchão') || name.includes('colchao')) return 'colchoes';
    return 'complementos';
}

function fixFile(filepath, getCatFunc) {
    if (!fs.existsSync(filepath)) return;
    let content = fs.readFileSync(filepath, 'utf-8');
    
    let result = content.replace(/<a([^>]*class="[^"]*product[^"]*"[^>]*)>/g, (match, p1) => {
        // Find the following h3 within the product block, roughly
        // Since we are doing regex on html, we need to locate the name.
        return match;
    });
    // Regular expression replacing isn't safe for HTML with nested tags
}

fixFile('quartos.html', getCategoryQuartos);
fixFile('salas.html', getCategorySalas);
fixFile('colchoes.html', getCategoryColchoes);
