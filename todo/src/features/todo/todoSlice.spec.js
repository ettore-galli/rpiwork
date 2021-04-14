import todoReducer, {
  createEntry,
  addEntry,
  deleteEntry,
  selectEntries,
} from './todoSlice';

describe('todo reducer', () => {
  const initialState = {
    entries: [],
    status: 'idle',
  };
  it('should handle initial state', () => {
    expect(todoReducer(undefined, { type: 'unknown' })).toEqual({
      entries: [],
      status: 'idle',
    });
  });

  it('should handle addEntry', () => {
    const actual = todoReducer(initialState, addEntry({ id: 1, text: "Test Add" }));
    expect(actual.entries).toEqual([
      { id: 1, text: "Test Add" }
    ]);
  });
  const initialStateWithEntries = {
    entries: [
      { id: 1, text: "Test entry 1" },
      { id: 2, text: "Test entry 2" },
      { id: 3, text: "Test entry 3" },
    ],
    status: 'idle',
  };
  it('should handle deleteEntry', () => {
    const actual = todoReducer(initialStateWithEntries, deleteEntry({ id: 2, text: "Test entry 2" }));
    expect(actual.entries).toEqual([
      { id: 1, text: "Test entry 1" },
      { id: 3, text: "Test entry 3" },
    ]);
  });


});
