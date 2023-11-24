function solution(bandage, health, attacks) {
    var maxTime = attacks[attacks.length - 1][0];
    var currentHealth = health;
    var attackIndexObj = {};
    var successive = 0;
    
    for (var i = 0; i < attacks.length; i++){
        attackIndexObj[attacks[i][0]] = attacks[i][1];
    }
    
    for (var i = 0; i <= maxTime; i++){
        if (i in attackIndexObj){
            currentHealth -= attackIndexObj[i];
            successive = 0
            
            if (currentHealth <= 0){
                return -1;
            }
        } else {
            successive += 1;
            if (successive < bandage[0]){
                currentHealth += bandage[1];
                if (currentHealth > health){
                    currentHealth = health;
                }
            } else {
                currentHealth = currentHealth + bandage[1] + bandage[2];
                if (currentHealth > health){
                    currentHealth = health;
                }
                successive = 0;
            }
        }
    }
    return currentHealth;
}