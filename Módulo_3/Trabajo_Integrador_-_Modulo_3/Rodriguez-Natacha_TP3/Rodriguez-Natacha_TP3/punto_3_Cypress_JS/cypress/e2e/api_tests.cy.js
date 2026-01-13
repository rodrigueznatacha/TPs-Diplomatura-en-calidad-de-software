let berry1_size = 20; 
const BASE_URL = 'https://pokeapi.co/api/v2/';

describe('API Tests - PokeAPI Berries y Pokemon', () => {

    // CASO 1: berry/1 (Validación de igualdad)
    it('Caso 1: Verifica el size (20), soil_dryness (15) y firmness (soft) de berry/1', () => {
        
        cy.request('GET', `${BASE_URL}berry/1`).then((response) => {
            // Verificar Status Code 200
            expect(response.status).to.equal(200); 

            // Verificar size, soil_dryness y firmness.name
            expect(response.body.size).to.equal(20); 
            expect(response.body.soil_dryness).to.equal(15);
            expect(response.body.firmness.name).to.equal('soft');
        });
    });

    // CASO 2: berry/2 (Validación comparativa)
    it('Caso 2: Verifica que el size de berry/2 sea MAYOR que berry/1 y que soil_dryness sea igual', () => {
        
        cy.request('GET', `${BASE_URL}berry/2`).then((response) => {
            expect(response.status).to.equal(200);

            // Verificar que en firmness, el name sea super-hard
            expect(response.body.firmness.name).to.equal('super-hard');

            // Verificar que el size sea mayor al del punto anterior 
            expect(response.body.size).to.be.greaterThan(berry1_size);

            // Verificar que el soil_dryness sea igual al del punto anterior (15)
            expect(response.body.soil_dryness).to.equal(15);
        });
    });

    // CASO 3: pokemon/pikachu (Validación de rango y tipos en lista)
    it('Caso 3: Verifica que base_experience esté en rango (10-1000) y que su tipo sea "electric"', () => {
        
        cy.request('GET', `${BASE_URL}pokemon/pikachu/`).then((response) => {
            expect(response.status).to.equal(200);

            const base_experience = response.body.base_experience;
            
            // Verificar que su experiencia base es mayor a 10 y menor a 1000 
            expect(base_experience).to.be.greaterThan(10);
            expect(base_experience).to.be.lessThan(1000); 

            // Verificar que su tipo es "electric" (búsqueda en un array de objetos)
            const isElectric = response.body.types.some(typeInfo => typeInfo.type.name === 'electric');
            
            expect(isElectric).to.be.true;
        });
    });
});