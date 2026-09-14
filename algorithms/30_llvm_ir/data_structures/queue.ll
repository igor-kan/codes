; ModuleID = 'algorithms/02_c/data_structures/queue.c'
source_filename = "algorithms/02_c/data_structures/queue.c"
target datalayout = "e-m:e-p270:32:32-p271:32:32-p272:64:64-i64:64-i128:128-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-linux-gnu"

; Function Attrs: mustprogress nofree norecurse nosync nounwind sspstrong willreturn memory(argmem: readwrite) uwtable
define dso_local void @enqueue(ptr noundef captures(none) %0, i32 noundef %1) local_unnamed_addr #0 {
  %3 = getelementptr inbounds nuw i8, ptr %0, i64 4004
  %4 = load i32, ptr %3, align 4, !tbaa !9
  %5 = add nsw i32 %4, 1
  %6 = srem i32 %5, 1000
  %7 = sext i32 %4 to i64
  %8 = getelementptr inbounds i32, ptr %0, i64 %7
  store i32 %6, ptr %8, align 4, !tbaa !5
  %9 = getelementptr inbounds nuw i8, ptr %0, i64 4008
  %10 = load i32, ptr %9, align 4, !tbaa !11
  %11 = add nsw i32 %10, 1
  store i32 %11, ptr %9, align 4, !tbaa !11
  ret void
}

; Function Attrs: mustprogress nofree norecurse nosync nounwind sspstrong willreturn memory(argmem: readwrite) uwtable
define dso_local i32 @dequeue(ptr noundef captures(none) %0) local_unnamed_addr #0 {
  %2 = getelementptr inbounds nuw i8, ptr %0, i64 4000
  %3 = load i32, ptr %2, align 4, !tbaa !12
  %4 = sext i32 %3 to i64
  %5 = getelementptr inbounds i32, ptr %0, i64 %4
  %6 = load i32, ptr %5, align 4, !tbaa !5
  %7 = add nsw i32 %3, 1
  %8 = srem i32 %7, 1000
  store i32 %8, ptr %2, align 4, !tbaa !12
  %9 = getelementptr inbounds nuw i8, ptr %0, i64 4008
  %10 = load i32, ptr %9, align 4, !tbaa !11
  %11 = add nsw i32 %10, -1
  store i32 %11, ptr %9, align 4, !tbaa !11
  ret i32 %6
}

attributes #0 = { mustprogress nofree norecurse nosync nounwind sspstrong willreturn memory(argmem: readwrite) uwtable "min-legal-vector-width"="0" "no-trapping-math"="true" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+cmov,+cx8,+fxsr,+mmx,+sse,+sse2,+x87" "tune-cpu"="generic" }

!llvm.module.flags = !{!0, !1, !2, !3}
!llvm.ident = !{!4}
!llvm.errno.tbaa = !{!5}

!0 = !{i32 1, !"wchar_size", i32 4}
!1 = !{i32 8, !"PIC Level", i32 2}
!2 = !{i32 7, !"PIE Level", i32 2}
!3 = !{i32 7, !"uwtable", i32 2}
!4 = !{!"clang version 22.1.8"}
!5 = !{!6, !6, i64 0}
!6 = !{!"int", !7, i64 0}
!7 = !{!"omnipotent char", !8, i64 0}
!8 = !{!"Simple C/C++ TBAA"}
!9 = !{!10, !6, i64 4004}
!10 = !{!"", !7, i64 0, !6, i64 4000, !6, i64 4004, !6, i64 4008}
!11 = !{!10, !6, i64 4008}
!12 = !{!10, !6, i64 4000}
