; ModuleID = 'algorithms/02_c/graphs/dfs.c'
source_filename = "algorithms/02_c/graphs/dfs.c"
target datalayout = "e-m:e-p270:32:32-p271:32:32-p272:64:64-i64:64-i128:128-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-linux-gnu"

@visited = dso_local local_unnamed_addr global [100 x i32] zeroinitializer, align 16
@.str = private unnamed_addr constant [4 x i8] c"%d \00", align 1

; Function Attrs: nofree nounwind sspstrong uwtable
define dso_local void @dfs(ptr noundef readonly captures(none) %0, i32 noundef %1, i32 noundef %2) local_unnamed_addr #0 {
  %4 = sext i32 %2 to i64
  %5 = getelementptr inbounds i32, ptr @visited, i64 %4
  store i32 1, ptr %5, align 4, !tbaa !5
  %6 = tail call i32 (ptr, ...) @printf(ptr noundef nonnull dereferenceable(1) @.str, i32 noundef %2)
  %7 = icmp sgt i32 %1, 0
  br i1 %7, label %8, label %11

8:                                                ; preds = %3
  %9 = getelementptr inbounds [100 x i32], ptr %0, i64 %4
  %10 = zext nneg i32 %1 to i64
  br label %12

11:                                               ; preds = %23, %3
  ret void

12:                                               ; preds = %8, %23
  %13 = phi i64 [ 0, %8 ], [ %24, %23 ]
  %14 = getelementptr inbounds nuw i32, ptr %9, i64 %13
  %15 = load i32, ptr %14, align 4, !tbaa !5
  %16 = icmp eq i32 %15, 0
  br i1 %16, label %23, label %17

17:                                               ; preds = %12
  %18 = getelementptr inbounds nuw i32, ptr @visited, i64 %13
  %19 = load i32, ptr %18, align 4, !tbaa !5
  %20 = icmp eq i32 %19, 0
  br i1 %20, label %21, label %23

21:                                               ; preds = %17
  %22 = trunc nuw nsw i64 %13 to i32
  tail call void @dfs(ptr noundef nonnull %0, i32 noundef %1, i32 noundef %22)
  br label %23

23:                                               ; preds = %12, %17, %21
  %24 = add nuw nsw i64 %13, 1
  %25 = icmp eq i64 %24, %10
  br i1 %25, label %11, label %12, !llvm.loop !9
}

; Function Attrs: nofree nounwind
declare noundef i32 @printf(ptr noundef readonly captures(none), ...) local_unnamed_addr #1

attributes #0 = { nofree nounwind sspstrong uwtable "min-legal-vector-width"="0" "no-trapping-math"="true" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+cmov,+cx8,+fxsr,+mmx,+sse,+sse2,+x87" "tune-cpu"="generic" }
attributes #1 = { nofree nounwind "no-trapping-math"="true" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+cmov,+cx8,+fxsr,+mmx,+sse,+sse2,+x87" "tune-cpu"="generic" }

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
!9 = distinct !{!9, !10}
!10 = !{!"llvm.loop.mustprogress"}
