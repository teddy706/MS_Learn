import React, { useState, useEffect } from 'react';
import { X, Save, Trash2, FileText } from 'lucide-react';

export default function QuickNotesModal({ unit, currentNote, onSave, onClose }) {
  const [noteText, setNoteText] = useState(currentNote || '');

  useEffect(() => {
    setNoteText(currentNote || '');
  }, [currentNote, unit]);

  if (!unit) return null;

  const handleSave = () => {
    onSave(unit.id, noteText);
    onClose();
  };

  const handleDelete = () => {
    if (confirm('작성하신 메모를 삭제하시겠습니까?')) {
      onSave(unit.id, '');
      onClose();
    }
  };

  return (
    <div className="modal-overlay" onClick={onClose}>
      <div className="modal-content" onClick={(e) => e.stopPropagation()}>
        <div className="modal-header">
          <div style={{ display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
            <FileText className="text-primary" size={20} />
            <h3 style={{ fontSize: '1.1rem', fontWeight: 700 }}>학습 노트: {unit.title}</h3>
          </div>
          <button className="btn-icon" style={{ width: '32px', height: '32px' }} onClick={onClose}>
            <X size={18} />
          </button>
        </div>

        <textarea
          className="notes-textarea"
          placeholder="이 단원에서 학습한 핵심 내용, 시험 출제 포인트, 또는 궁금한 점을 메모해 보세요..."
          value={noteText}
          onChange={(e) => setNoteText(e.target.value)}
          autoFocus
        />

        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
          {currentNote ? (
            <button className="btn btn-secondary" style={{ color: '#ef4444' }} onClick={handleDelete}>
              <Trash2 size={16} />
              <span>메모 삭제</span>
            </button>
          ) : <div />}

          <div style={{ display: 'flex', gap: '0.5rem' }}>
            <button className="btn btn-secondary" onClick={onClose}>
              취소
            </button>
            <button className="btn btn-primary" onClick={handleSave}>
              <Save size={16} />
              <span>저장하기</span>
            </button>
          </div>
        </div>
      </div>
    </div>
  );
}
