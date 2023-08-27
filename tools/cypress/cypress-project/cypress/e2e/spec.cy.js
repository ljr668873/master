describe('template spec', () => {

  before(()=>{
    Cypress.on("uncaught:exception", (err, runnable) => {
      // returning false here prevents Cypress from
      // failing the test
      return false;
    });
  })

  it('test_登录成功并搜索显示工具共1条', () => {
    cy.visit('http://172.30.0.90/next')
    cy.contains("普通登录").should("be.visible");
    cy.get("#general_login_username").type("easyops");
    cy.get("#general_login_password").type("easyops");
    cy.get('button[type="submit"]').click();
    cy.contains("test",{timeout:10000}).should("be.visible");
    cy.get('[data-testid="list-search"]').find("input").eq(1).type("test工具{enter}");
    cy.contains("共 1 条").should("be.visible");
    
  })
})