// Setting the level to play
let difficulty = sessionStorage.getItem('difficulty');
if (difficulty != 0) {
  if (difficulty > 3) {
    levelToPlay=1;
    leftStaff=[3, 2, 1];
  } else if (difficulty == 3) {
    levelToPlay=2;
    leftStaff=[5, 4, 3, 2, 1];
  } else {
    levelToPlay=3;
    leftStaff=[7, 6, 5, 4, 3, 2, 1];
  }
}