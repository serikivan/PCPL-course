use std::io;
use std::process::Command;

// Функция для вывода игровой доски
fn print_board(board: &Vec<Vec<char>>) {
    // Очистка консоли
    if cfg!(windows) {
        let _ = Command::new("cmd").arg("/c").arg("cls").status();
    } else {
        let _ = Command::new("sh").arg("-c").arg("clear").status();
    }

    // Перерисовка обновленной игровой доски
    println!("  1 2 3");
    for (i, row) in board.iter().enumerate() {
        print!("{} ", i + 1);
        for &cell in row {
            print!("{} ", cell);
        }
        println!();
    }
}

// Проверка победителя
fn is_winner(board: &Vec<Vec<char>>, player: char) -> bool {
    // Проверка строк и столбцов
    for i in 0..3 {
        if (1..=3).all(|j| board[i][j - 1] == player) || (1..=3).all(|j| board[j - 1][i] == player) {
            return true;
        }
    }

    // Проверка диагоналей
    if (1..=3).all(|i| board[i - 1][i - 1] == player) || (1..=3).all(|i| board[i - 1][3 - i] == player) {
        return true;
    }

    false
}

// Проверка ничьей
fn is_draw(board: &Vec<Vec<char>>) -> bool {
    board.iter().all(|row| row.iter().all(|&cell| cell != ' '))
}

fn main() {
    loop {
        // Инициализация игровой доски
        let mut board = vec![
            vec![' ', ' ', ' '],
            vec![' ', ' ', ' '],
            vec![' ', ' ', ' '],
        ];

        let mut current_player = 'X';

        loop {
            print_board(&board);

            println!("Ход игрока {}", current_player);

            println!("Введите ход (например, 12 для строки 1, столбца 2): ");
            let mut input = String::new();
            io::stdin().read_line(&mut input).expect("Не удалось прочитать строку");

            // Обработка введенного хода
            let trimmed_input = input.trim();
            if trimmed_input.len() == 2 {
                if let (Some(row), Some(col)) = (trimmed_input.chars().nth(0).unwrap().to_digit(10), trimmed_input.chars().nth(1).unwrap().to_digit(10)) {
                    let (row, col) = (row as usize, col as usize);

                    // Проверка корректности введенных координат
                    if row >= 1 && row <= 3 && col >= 1 && col <= 3 {
                        // Проверка, что выбранная клетка свободна
                        if board[row - 1][col - 1] == ' ' {
                            // Установка символа игрока на доску
                            board[row - 1][col - 1] = current_player;

                            // Проверка победителя
                            if is_winner(&board, current_player) {
                                print_board(&board);
                                println!("Игрок {} выиграл!", current_player);
                                break;
                            }

                            // Проверка ничьей
                            if is_draw(&board) {
                                print_board(&board);
                                println!("Ничья!");
                                break;
                            }

                            // Смена хода игрока
                            current_player = if current_player == 'X' { 'O' } else { 'X' };
                        } else {
                            println!("Клетка уже занята. Попробуйте снова.");
                        }
                    } else {
                        println!("Неверный ввод. Пожалуйста, введите числа от 1 до 3.");
                    }
                }
            } else {
                println!("Неверный формат ввода. Пожалуйста, введите двузначное число.");
            }
        }

        // Вопрос о продолжении
        println!("Хотите сыграть еще раз? (y/n)");
        let mut choice = String::new();
        io::stdin().read_line(&mut choice).expect("Не удалось прочитать строку");
        if !choice.trim().eq_ignore_ascii_case("y") {
            break;
        }
    }

    println!("Нажмите Enter для выхода...");
    let mut input = String::new();
    io::stdin().read_line(&mut input).expect("Не удалось прочитать строку");
}
