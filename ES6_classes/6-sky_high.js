import Building from './5-building';

export default class SkyHighBuilding extends Building {
  constructor(sqft, floors) {
    super(sqft);
    this.floors = floors;
  }

  get floors() { return this._floors; }

  set floors(newValue) { this._floors = newValue; }

  evacuationWarningMessage() { return `Evacuate slowly the ${this._floors} floors`; }
}
