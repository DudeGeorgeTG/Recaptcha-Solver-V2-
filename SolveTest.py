from solver import Solver

solution = Solver(
    '6Ldx7ZkUAAAAAF3SZ05DRL2Kdh911tCa3qFP0-0r',
    'https://co.pinterest.com'
)
token = solution.token()

print('Solved', solution.solvedTime, 'Token:', token)
