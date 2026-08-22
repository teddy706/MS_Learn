import React, { useState } from 'react';
import { HelpCircle, Eye, EyeOff, Sparkles } from 'lucide-react';

export default function Flashcards({ flashcardsData }) {
  const [flippedIds, setFlippedIds] = useState([]);
  const [selectedTag, setSelectedTag] = useState('All');

  const toggleFlip = (id) => {
    setFlippedIds(prev => 
      prev.includes(id) ? prev.filter(i => i !== id) : [...prev, id]
    );
  };

  const tags = ['All', ...new Set(flashcardsData.flatMap(f => f.tags))];

  const filteredCards = selectedTag === 'All' 
    ? flashcardsData 
    : flashcardsData.filter(f => f.tags.includes(selectedTag));

  return (
    <div>
      <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', marginBottom: '1.5rem', flexWrap: 'wrap', gap: '1rem' }}>
        <div>
          <h2 style={{ fontSize: '1.25rem', fontWeight: 700, display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
            <Sparkles className="text-primary" size={20} style={{ color: 'var(--primary)' }} />
            <span>AB-100 핵심 아키텍처 플래시 카드</span>
          </h2>
          <p style={{ fontSize: '0.88rem', color: 'var(--text-muted)' }}>
            카드를 클릭하여 핵심 정답과 해설을 확인해 보세요.
          </p>
        </div>

        {/* Tag Filters */}
        <div style={{ display: 'flex', gap: '0.4rem', flexWrap: 'wrap' }}>
          {tags.map(tag => (
            <button
              key={tag}
              className={`btn ${selectedTag === tag ? 'btn-primary' : 'btn-secondary'}`}
              style={{ padding: '0.35rem 0.75rem', fontSize: '0.8rem', borderRadius: 'var(--radius-full)' }}
              onClick={() => setSelectedTag(tag)}
            >
              #{tag}
            </button>
          ))}
        </div>
      </div>

      <div className="flashcards-wrapper">
        {filteredCards.map(card => {
          const isFlipped = flippedIds.includes(card.id);

          return (
            <div 
              key={card.id} 
              className="flashcard"
              onClick={() => toggleFlip(card.id)}
            >
              <div>
                <div className="flashcard-header">
                  <span className="flashcard-cat">{card.category}</span>
                  <span style={{ fontSize: '0.8rem', color: 'var(--text-muted)', display: 'flex', alignItems: 'center', gap: '0.25rem' }}>
                    {isFlipped ? <EyeOff size={14} /> : <Eye size={14} />}
                    {isFlipped ? '숨기기' : '정답 보기'}
                  </span>
                </div>

                <div className="flashcard-question">
                  <HelpCircle size={18} style={{ color: 'var(--primary)', display: 'inline', marginRight: '6px' }} />
                  {card.question}
                </div>
              </div>

              {isFlipped ? (
                <div className="flashcard-answer">
                  <strong>💡 핵심 해설:</strong>
                  <div style={{ marginTop: '0.4rem' }}>{card.answer}</div>
                </div>
              ) : (
                <div style={{ fontSize: '0.82rem', color: 'var(--text-muted)', textAlign: 'center', padding: '1rem', border: '1px dashed var(--border-light)', borderRadius: 'var(--radius-md)' }}>
                  👆 카드를 클릭하면 정답이 나타납니다.
                </div>
              )}

              <div style={{ display: 'flex', gap: '0.3rem', marginTop: '0.75rem', flexWrap: 'wrap' }}>
                {card.tags.map(t => (
                  <span key={t} style={{ fontSize: '0.72rem', color: 'var(--text-muted)', backgroundColor: 'var(--bg-subtle)', padding: '0.15rem 0.4rem', borderRadius: '4px' }}>
                    #{t}
                  </span>
                ))}
              </div>
            </div>
          );
        })}
      </div>
    </div>
  );
}
