# AIproject
### Checkers
#### PEAS
| Agent Type    | Performance Measure |        Environment       |       Actuators      |  Sensors    |
| :---:         |     :---:           |           :---:          |      :---:           |       :--:  |
| Checkers Game | Win over Opponent   | Board & Pieces & Players | General rules of Game| Move Pieces |
#### ODESA
| Task Environment | Observable | Agents | Deterministic | Episodic   | Static | Discrete |
| :---:            |     :---:  | :---:  |  :---:        |  :--:      | :--:   | :--:     |
| Checkers Game    |   Fully    | Multi  | Deterministic | Sequential | Static | Discrete |
#### The Structure of Agents
Utility-based agents
#### Formulating problems
- States: A state description specifies the location of each of the 12 pieces for every player
- Initial state: Any state can be designated as the initial state.
- Actions: A move consists of moving a piece diagonally to an adjacent unoccupied square.
- Transition model: Given a state and action, this returns the resulting state; for example, One of player move pieces.
- Goal test: Win the game by made Opponent without pieces remaining, or who cannot move due to being blocked, loses the game.
- Path cost: Each step costs 1, so the path cost is the number of steps in the path.

TO KNOW MORE ABOUT GAME.[^1].
[^1]: https://en.wikipedia.org/wiki/Checkers
