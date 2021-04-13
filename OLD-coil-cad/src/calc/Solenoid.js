

function inductance(mur, lunghezza, diametro, spire) {
  return 1.25663706212e-6 * mur * Math.pow(spire, 2) * 3.1415 * Math.pow(diametro / 2, 2) / lunghezza
}

export default inductance;
